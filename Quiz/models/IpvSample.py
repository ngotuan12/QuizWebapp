'''
Created on May 13, 2024

@author: NGO ANH TUAN
'''

from django.db import models


class IpvSample(models.Model):
    create_date = models.DateTimeField(auto_now_add=True,db_column="create_date")
    src_image_path = models.CharField(max_length=200)
    threshold_image_path = models.CharField(max_length=200)
    gauss_image_path = models.CharField(max_length=200)
    noise_image_path = models.CharField(max_length=200)
    text_content = models.CharField(max_length=500)
    name = models.CharField(max_length=200)
    class Meta:
        db_table = 'ipv_sample'
