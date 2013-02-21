#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.contrib import admin
from django.conf.urls import patterns
from django.utils.translation import ugettext as _
from voip_gateway.models import Gateway, Provider
from common.app_label_renamer import AppLabelRenamer
AppLabelRenamer(native_app_label=u'voip_gateway', app_label=_('Voip Gateway')).main()


class GatewayAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Gateway Detail'), {
            'fields': ('name', 'description', 'addprefix', 'removeprefix',
                       'protocol', 'hostname', 'secondused', 'failover',
                       'addparameter', 'count_call', 'count_using',
                       'maximum_call', 'status', 'max_call_gateway'),
        }),
    )
    list_display = ('id', 'name', 'protocol', 'hostname', 'addprefix',
                    'removeprefix', 'secondused', 'count_call')
    list_display_links = ('name', )
    list_filter = ['protocol', 'hostname']
    ordering = ('id', )

    def get_urls(self):
        urls = super(GatewayAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^$', self.admin_site.admin_view(self.changelist_view)),
            (r'^add/$', self.admin_site.admin_view(self.add_view)),
            (r'^/(.+)/$', self.admin_site.admin_view(self.change_view)),
        )
        return my_urls + urls

    def changelist_view(self, request, extra_context=None):
        """
        VoIP Gateway Listing
        """
        ctx = {
            'app_label': _('VoIP Gateway'),
        }
        return super(GatewayAdmin, self).changelist_view(request, extra_context=ctx)

    def add_view(self, request, extra_context=None):
        """
        Add VoIP Gateway
        """
        ctx = {
            'app_label': _('VoIP Gateway'),
        }
        return super(GatewayAdmin, self).add_view(request, extra_context=ctx)

    def change_view(self, request, object_id, extra_context=None):
        """
        Edit VoIP Gateway
        """
        ctx = {
            'app_label': _('VoIP Gateway'),
        }
        return super(GatewayAdmin, self).change_view(request, object_id, extra_context=ctx)
admin.site.register(Gateway, GatewayAdmin)


class ProviderAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Provider Detail'), {
            #'classes':('collapse', ),
            'fields': ('name', 'description', 'gateway', 'metric'),
        }),
    )
    list_display = ('id', 'name', 'gateway', 'metric', 'updated_date')
    list_display_links = ('name', )
    list_filter = ['gateway', 'metric']
    ordering = ('id', )

    def get_urls(self):
        urls = super(ProviderAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^$', self.admin_site.admin_view(self.changelist_view)),
            (r'^add/$', self.admin_site.admin_view(self.add_view)),
            (r'^/(.+)/$', self.admin_site.admin_view(self.change_view)),
        )
        return my_urls + urls

    def changelist_view(self, request, extra_context=None):
        """
        VoIP Provider Listing
        """
        ctx = {
            'app_label': _('VoIP Gateway'),
        }
        return super(ProviderAdmin, self).changelist_view(request, extra_context=ctx)

    def add_view(self, request, extra_context=None):
        """
        Add VoIP Provider
        """
        ctx = {
            'app_label': _('VoIP Gateway'),
        }
        return super(ProviderAdmin, self).add_view(request, extra_context=ctx)

    def change_view(self, request, object_id, extra_context=None):
        """
        Edit VoIP Gateway
        """
        ctx = {
            'app_label': _('VoIP Gateway'),
        }
        return super(ProviderAdmin, self).change_view(request, object_id, extra_context=ctx)

admin.site.register(Provider, ProviderAdmin)
