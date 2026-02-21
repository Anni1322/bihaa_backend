from django.db import models

class CommunityBiodata(models.Model):
    # Meta Information
    created_at = models.DateTimeField(auto_now_add=True)
    serial_number = models.CharField(
        max_length=50, 
        unique=True,
        verbose_name="सरल क्रमांक (Serial Number)"
    )

    # NEW: Image Field
    profile_photo = models.ImageField(
        upload_to='biodata_photos/', 
        verbose_name="फोटो (Photo)", 
        blank=True, 
        null=True
    )

    # Personal Details
    full_name = models.CharField(max_length=255, verbose_name="नाम (Name)")
    caste = models.CharField(max_length=100, verbose_name="जाति (Caste)", default="Gond")
    gotra = models.CharField(max_length=100, verbose_name="गोत्र (Gotra)")
    deity_number = models.CharField(max_length=50, verbose_name="देव संख्या (Deity Number)")
    
    # Family Details
    father_name = models.CharField(max_length=255, verbose_name="पिता का नाम (Father's Name)")
    mother_name = models.CharField(max_length=255, verbose_name="माता का नाम (Mother's Name)")
    maternal_uncle_gotra = models.CharField(max_length=100, verbose_name="मामा का गोत्र (Mama Gotra)")
    family_status = models.TextField(verbose_name="पारिवारिक स्थिति (Family Status)")

    # Physical Attributes
    complexion = models.CharField(max_length=50, verbose_name="रंग (Complexion)")
    height = models.CharField(max_length=20, verbose_name="कद (Height)")
    date_of_birth = models.DateField(verbose_name="जन्मतिथि (Date of Birth)")

    # Professional & Educational
    education = models.TextField(verbose_name="शिक्षा (Education)")
    occupation = models.CharField(max_length=255, verbose_name="वर्तमान व्यवसाय", default="निरंक")

    # Contact & Address
    address = models.TextField(verbose_name="पूरा पता (Address)")
    guardian_mobile = models.CharField(max_length=15, verbose_name="पालक का मोबाईल (Mobile)")

    def __str__(self):
        return f"{self.serial_number} - {self.full_name}"

    class Meta:
        verbose_name = "Biodata Profile"
        verbose_name_plural = "Biodata Profiles"
        ordering = ['-created_at']
        
        
        

  