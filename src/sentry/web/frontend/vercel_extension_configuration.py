from __future__ import absolute_import


from sentry.integrations.pipeline import IntegrationPipeline
from sentry.web.frontend.base import BaseView


class VercelExtensionConfigurationView(BaseView):
    auth_required = False

    def get(self, request, *args, **kwargs):
        # TODO: check org and login status
        org = request.user.get_orgs()[0]

        pipeline = self.init_pipeline(request, org, request.GET)

        return pipeline.current_step()

    def init_pipeline(self, request, organization, params):
        pipeline = IntegrationPipeline(
            request=request, organization=organization, provider_key="vercel"
        )

        pipeline.initialize()
        pipeline.bind_state("vercel", params)

        return pipeline
