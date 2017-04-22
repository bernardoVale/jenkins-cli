
def run(args, server):
    job = args.job

    print("Calling job {}".format(job))
    server.build_job(job)
    print("Build triggered!")
    # last_build_number = server.get_job_info(job)['lastCompletedBuild']['number']



