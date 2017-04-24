

def script(args, server):
    if args.script:
        with open(args.script) as reader:
            content = reader.read()
            output = server.run_script(content)
            print(output)
            return None
    print("script parameter is mandatory")