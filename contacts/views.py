from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(req):
    if req.method == 'POST':
        listing_id = req.POST['listing_id']
        listing = req.POST['listing']
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        message = req.POST['message']
        user_id = req.POST['user_id']
        realtor_email = req.POST['realtor_email']

        if req.user.is_authenticated:
            user_id = req.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(req, 'You have already made one inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # send_mail('Property Listing Inquiry',
        #     'There has been inquiry for' + listing,
        #     'aayush.shah912@gmail.com',
        #     [realtor_email],
        #     fail_silently=False
        # )
        
        messages.success(req, 'Request submitted, realtor will reach to you soon')
        return redirect('/listings/'+listing_id)
    return