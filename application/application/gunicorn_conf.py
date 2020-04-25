# from pprint import pprint

# this is the default one
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# access_log_format = '%%({X-REAL-IP}i)s %%(l)s %%(u)s %%(t)s "%%(r)s" %%(s)s %%(b)s "%%(f)s" "%%(a)s"'
# access_log_format = '%%({X-Forwarded-For}i)s'
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# access_log_format = '%({X-SSL-CERT}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

workers = 1
worker_class = 'gthread'
# if thread >1 gthread is used automatically
threads = 1

errorlog = "-"
accesslog = "-"

# def pre_request(worker, req):
    # req.body.worker_id = worker.pid

    # print("These are the attributes of req")
    # pprint(vars(req))
    # print("End of attributes for req.\n")

    # print("These are the attributes of worker")
    # pprint(vars(worker))
    # print("End of attributes for worker.\n")
