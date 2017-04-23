

def list_jobs(args, server):
    jobs = server.get_job_info_regex(pattern=args.pattern, folder_depth=None)
    for job in jobs:
        color = job['color']
        url = job['url']
        in_queue = job['inQueue']
        name = job['displayName']
        print("Name:{} In Queue:{} Status:{} URL:{}".format(name, in_queue, color, url))