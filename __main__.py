import uvicorn
from uvicorn.config import LOGGING_CONFIG

if __name__ == '__main__':
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = '%(asctime)s [%(name)s] %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'

    portnum = 11567
    uvicorn.run("main:app", host="0.0.0.0", port=portnum, reload=True, workers=100)