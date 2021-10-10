from django.db import models



class PollingUnit(models.Model):
    polling_unit_id = models.IntegerField(null=False, blank=False)
    ward_id = models.IntegerField(null=False, blank=False)
    lga_id = models.IntegerField(null=False, blank=False)
    uniquewardid = models.IntegerField(null=False, blank=False)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField(null=True)
    lat = models.CharField(max_length=255, null=False, blank=False)
    long = models.CharField(max_length=255, null=False, blank=False)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.TextField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50, null=True)
    
    
    class Meta:
        db_table = 'polling_unit'
        
    def __str__(self):
        return "{}".format(self.id)


class AgentName(models.Model):
    polling_unit = models.BigIntegerField()
    firstname = models.CharField(max_length=255, null=False, blank=False)
    lastname = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=13, null=False)
    
    class Meta:
        db_table = 'agentname'
        
    def __str__(self):
        return "{}".format(self.id)
    
    

class AnnouncedLgaResult(models.Model):
    lga_name = models.CharField(max_length=50, null=False, blank=False)
    party_abbreviation = models.CharField(max_length=4, null=False, blank=False)
    party_score = models.IntegerField(null=False, blank=False)
    entered_by_user = models.CharField(max_length=50, null=False, blank=False)
    date_entered = models.TextField(null=False, blank=False)
    user_ip_address = models.CharField(max_length=50, blank=False, null=False)
    
    class Meta:
        db_table = 'announced_lga_results'
        
    def __str__(self):
        return "{}".format(self.id)
    

class AnnouncedPUResult(models.Model):
    polling_unit = models.BigIntegerField()
    party_abbreviation = models.CharField(max_length=4, null=False, blank=False)
    party_score = models.IntegerField(null=False, blank=False)
    entered_by_user = models.CharField(max_length=50, null=False, blank=False)
    date_entered = models.TextField(null=False, blank=False)
    user_ip_address = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        db_table = 'announced_pu_results'
    
    
    def __str__(self):
        return "{}".format(self.id)
    
    

class AnnouncedStateResult(models.Model):
    state_name = models.CharField(max_length=50, null=False, blank=False)
    party_abbreviation = models.CharField(max_length=4, null=False, blank=False)
    party_score = models.IntegerField(null=False, blank=False)
    entered_by_user = models.CharField(max_length=50, null=False, blank=False)
    date_entered = models.DateTimeField(null=False, blank=False)
    user_ip_address = models.CharField(max_length=50, null=False, blank=False)
    
    
    class Meta:
        db_table = 'announced_state_results'
        
    def __str__(self):
        return "{}".format(self.id)
    
    

class AnnouncedWardResults(models.Model):
    ward_name = models.CharField(max_length=50, null=False, blank=False)
    party_abbreviation = models.CharField(max_length=4, null=False, blank=False)
    party_score = models.IntegerField(null=False, blank=False)
    entered_by_user = models.CharField(max_length=50, null=False, blank=False)
    date_entered = models.DateTimeField(null=False, blank=False)
    user_ip_address = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        db_table = 'announced_ward_results'
    
    def __str__(self):
        return "{}".format(self.id)
    


class Lga(models.Model):
    lga_id = models.IntegerField(null=False, blank=False)
    lga_name = models.CharField(max_length=50, null=False, blank=False)
    state_id = models.BigIntegerField(null=False, blank=False)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, null=False, blank=False)
    date_entered = models.TextField(null=False, blank=False)
    user_ip_address = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        db_table = 'lga'
    
    def __str__(self):
        return "{}".format(self.id)
    
    

class Party(models.Model):
    partyid = models.CharField(max_length=11, null=False, blank=False)
    partyname = models.CharField(max_length=11, null=False, blank=False)
    
    
    class Meta:
        db_table = 'party'
        
    def __str__(self):
        return "{}".format(self.id)
    


class State(models.Model):
    state_name = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        db_table = 'states'
    
    def __str__(self):
        return "{}".format(self.id)
    


class Ward(models.Model):
    ward_id = models.IntegerField(null=False, blank=False)
    ward_name = models.CharField(max_length=50, null=False, blank=False)
    lga_id = models.IntegerField(null=False, blank=False)
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, null=False, blank=False)
    date_entered = models.TextField(null=False, blank=False)
    user_ip_address = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        db_table = 'ward'
    
    def __str__(self):
        return "{}".format(self.id)