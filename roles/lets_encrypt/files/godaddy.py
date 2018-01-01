#!/usr/bin/env python3

import os
import sys
import configparser
import logging
import time
import godaddypy


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
config = configparser.ConfigParser()
config.read( os.path.join(__location__,'.gdkeys'))
api_key = config['API']['key']
api_secret = config['API']['secret']


my_acct = godaddypy.Account(api_key=api_key, api_secret=api_secret)
client = godaddypy.Client(my_acct)

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _get_zone(domain):
    parts = domain.split(".")
    zone_parts = parts[-2::]
    zone = ".".join(zone_parts)
    return zone


def _get_subdomain_for(domain, zone):
    subdomain = domain[0:(-len(zone)-1)]
    return subdomain


def _update_dns(domain, token):
    challengedomain = "_acme-challenge." + domain
    logger.info(" + Updating TXT record for {0} to '{1}'.".format(challengedomain, token))
    zone = _get_zone(challengedomain)
    # logger.info("Zone to update: {0}".format(zone))
    subdomain = _get_subdomain_for(challengedomain, zone)
    # logger.info("Subdomain name: {0}".format(subdomain))

    record = {
        'name': subdomain,
        'data': token,
        'ttl': 600,
        'type': 'TXT'
    }
    result = client.update_record(zone, record)
    if result is not True:
        logger.warn("Error updating record for domain {0}.".format(domain))
    time.sleep(60)

def create_txt_record(args):
    domain, token = args[0], args[2]
    _update_dns(domain, token)


def delete_txt_record(args):
    domain = args[0]
    # using client.delete_record() is dangerous. null it instead!
    # https://github.com/eXamadeus/godaddypy/issues/13

    if domain == "":
        logger.warn("Error deleting record, the domain argument is empty")
    else:
        _update_dns(domain, "null")


def deploy_cert(args):
    domain, privkey_pem, cert_pem, fullchain_pem, chain_pem, timestamp = args
    logger.info(' + ssl_certificate: {0}'.format(fullchain_pem))
    logger.info(' + ssl_certificate_key: {0}'.format(privkey_pem))
    return


def unchanged_cert(args):
    return


def invalid_challenge(args):
    [domain, response] = args
    logger.warn(" + invalid challenge for domain {0}: {1}".format(domain, response))
    return

def request_failure(args):
    [status_code, err_txt, req_type] = args
    logger.warn(" + Request failed with status code: {0}, {1}, type: {2}".format(status_code, err_txt, req_type))
    return

def exit_hook(args):
    pass

def startup_hook(args):
    pass


def main(argv):
    ops = {
        'deploy_challenge': create_txt_record,
        'clean_challenge' : delete_txt_record,
        'deploy_cert'     : deploy_cert,
        'unchanged_cert'  : unchanged_cert,
        'invalid_challenge': invalid_challenge,
        'request_failure' : request_failure,
        'exit_hook'       : exit_hook,
        'startup_hook'    : startup_hook,
    }
    logger.info(" + Godaddy hook executing: {0}".format(argv[0]))
    ops[argv[0]](argv[1:])


if __name__ == '__main__':
    main(sys.argv[1:])
