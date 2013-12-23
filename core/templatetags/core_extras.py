from django import template

register = template.Library()


icons_mapping = {
	"dashboard": "dashboard",
	"application": "desktop",
	"environment": "sitemap",
	"server": "puzzle-piece",
	"task": "tasks",
	"execution": "bars",
}

status_mapping = {
	"success": ["success", "check", "Success"],
	"running": ["warning", "spinner fa-spin", "Running"],
	"failed": ["danger", "exclamation-triangle", "Failed"],
}

@register.simple_tag
def model_icon(model):
    return '<i class="fa fa-'+icons_mapping[model]+'"></i>'

@register.simple_tag
def execution_status(status):
	template = '<span class="label label-%s"><i class="fa fa-%s"></i> %s</span>' % tuple(status_mapping[status])
	return template