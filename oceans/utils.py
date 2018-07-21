import digitalocean

from topcoder.settings import DIGITAL_OCEAN_TOKEN


def get_digital_data(file_object):
    manager = digitalocean.Manager(token=DIGITAL_OCEAN_TOKEN)
    my_droplets = manager.get_all_droplets()
    context = {}
    context['droplet_details'] = []

    for droplet in my_droplets:
        details = {}
        details['features'] = droplet.networks
        details['memory'] = droplet.memory
        details['created_at'] = droplet.created_at
        details['region'] = droplet.region
        details['size'] = droplet.size
        details['total_space'] = droplet.disk
        details['total_size'] = droplet.size

        context['droplet_details'].append(details)

    context['file_size'] = file_object.size
    return context
