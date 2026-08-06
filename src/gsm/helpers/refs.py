import flet as ft
from upu.helpers.buttons import extLinkBtn # XXX to transfer all upu.helpers in gsm.helpers

gh_url = 'http://GitHub.com/GrCOTE7/GSM'

def gh_link(color="LIGHT_GREEN_ACCENT_400"):
    gh_link = extLinkBtn("Dépôt GitHub", gh_url, "Va et fork le projet !", 'center')
    return gh_link
