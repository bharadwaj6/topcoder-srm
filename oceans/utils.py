import digitalocean

from topcoder.settings import DIGITAL_OCEAN_TOKEN


def get_digital_data(file_object):
    manager = digitalocean.Manager(token=DIGITAL_OCEAN_TOKEN)
    my_droplets = manager.get_all_droplets()
    droplet = my_droplets[0]

    context = {}
    context['droplet_options'] = {}
    context['droplet_options']['features'] = droplet.networks
    context['droplet_options']['memory'] = droplet.memory
    context['droplet_options']['created_at'] = droplet.created_at
    context['droplet_options']['region'] = droplet.region
    context['droplet_options']['size'] = droplet.size

    context['total_space'] = droplet.disk
    context['total_size'] = droplet.size

    context['file_size'] = file_object.size
    return context
