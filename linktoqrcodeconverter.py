#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyqrcode
import png
link=input("Kindly type the link you would like to convert to a qrcode: ")
qr_code = pyqrcode.create(link)
qr_code.png ("link.png", scale=5)
print('Your QR code has been generated successfully 😉')


# In[ ]:




