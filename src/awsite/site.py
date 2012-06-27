#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) 2012 Ville Korhonen <ville@xd.fi>

import sys
import os

import boto
#from boto.s3.connection import S3Connection
#from boto.s3.key import Key

from utils import mask_key

class Site(object):
    def __init__(self, aws_key_id=None, aws_secret_key=None):
        # TODO: Asetukset
        pass
    
    def _parse_config(self, config):
        # TODO: parsi annettu string (json?)
        pass
    
    def _read_config(self, filename):
        # TODO: lue asetukset annetusta tiedostosta (bucketit, cfdistid, avaimet, ...)
        pass 
    
    def create_site(self):
        # TODO: S3 Bucket (luo uusi; jos löytyy wanha, kysy korvataanko, uploadaa tyhjä template tai annettu kansio/tiedostot)
        # TODO: CF Distribution (luo uusi, aseta logitus, mahdolliset extrapolut / originit; luo joku cdn-alidomainmappaus, jotta voi jakaa lataukset useisiin domaineihin)
        # TODO: R53: aseta dns-tietueet (ypcs.fi => xxx.cloudfront.net; jos domainia ei löydy, kysy luodaanko uusi)
        # TODO: IAM keys (luo uudet avaimet, joilla pääsee uploadaamaan sisältöä)
        pass
    
    def remove_site(self):
        # TODO: poista (valintojen mukaan) IAM, R53, CF, S3 (CF, S3 vois vaatia varmistuksen)
        pass
    
    def upload_file(self, filename):
        # TODO: Uploadaa annettu tiedosto S3:een
        pass

def main():
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
