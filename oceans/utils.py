import digitalocean

from topcoder.settings import DIGITAL_OCEAN_TOKEN


def gb_to_mb(sz):
    return 1024 * sz


def size_in_mb(sz):
    return sz / 1024.0 / 1024.0


def get_best_droplet(my_droplets, file_size):
    """
    1. eliminate ones with less bandwidth/ free space than file size
    2. Check sizes of droplets and prefer the one with maximum size.
        If more than one droplet exists, use the one with max bandwidth.
    """
    bandwidths = []
    sizes = []

    for droplet in my_droplets:
        bandwidths.append(gb_to_mb(int(droplet.size['transfer'])))
        sizes.append(gb_to_mb(int(droplet.size['disk'])))

    invalid = []
    for i in range(len(bandwidths)):
        if bandwidths[i] or sizes[i] < file_size:
            invalid.append(i)

    best_sz = max(sizes)
    best_overall = None
    best_band = None
    for i in range(len(sizes)):
        if i not in invalid:
            sz = sizes[i]
            if sz == best_sz:
                if not best_overall:
                    best_overall = i
                if not best_band:
                    best_band = bandwidths[i]

                cur_band = bandwidths[i]
                if cur_band > best_band:
                    best_band = cur_band
                    best_overall = i

    return my_droplets[i], i

def get_all_droplets():
    manager = digitalocean.Manager(token=DIGITAL_OCEAN_TOKEN)
    my_droplets = manager.get_all_droplets()
    return my_droplets


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

    best_droplet, best_droplet_index = get_best_droplet(my_droplets, size_in_mb(file_object.size))
    context['best_droplet'] = best_droplet
    context['best_droplet_index'] = best_droplet_index

    return context


