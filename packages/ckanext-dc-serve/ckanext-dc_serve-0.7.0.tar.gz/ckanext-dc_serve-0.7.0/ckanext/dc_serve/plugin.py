from ckan.lib.jobs import _connect as ckan_redis_connect
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from flask import Blueprint
from rq.job import Job

from .cli import get_commands
from .jobs import generate_condensed_resource_job
from .route_funcs import dccondense
from .serve import dcserv

from dcor_shared import DC_MIME_TYPES


class DCServePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IClick)
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IActions, inherit=True)

    # IBlueprint
    def get_blueprint(self):
        """Return a Flask Blueprint object to be registered by the app."""

        # Create Blueprint for plugin
        blueprint = Blueprint(self.name, self.__module__)

        # Add plugin url rules to Blueprint object
        rules = [
            ('/dataset/<uuid:id>/resource/<uuid:resource_id>/condensed.rtdc',
             'dccondense',
             dccondense),
        ]
        for rule in rules:
            blueprint.add_url_rule(*rule)
        return blueprint

    # IClick
    def get_commands(self):
        return get_commands()

    # IResourceController
    def after_create(self, context, resource):
        """Generate condensed dataset"""
        if resource.get('mimetype') in DC_MIME_TYPES:
            pkg_job_id = f"{resource['package_id']}_{resource['position']}_"
            jid_condense = pkg_job_id + "condense"
            if not Job.exists(jid_condense, connection=ckan_redis_connect()):
                toolkit.enqueue_job(generate_condensed_resource_job,
                                    [resource],
                                    title="Create condensed dataset",
                                    queue="dcor-long",
                                    rq_kwargs={"timeout": 3600,
                                               "job_id": jid_condense})

    # IActions
    def get_actions(self):
        # Registers the custom API method defined above
        return {'dcserv': dcserv}
