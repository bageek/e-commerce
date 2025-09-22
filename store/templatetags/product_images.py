from django import template
from django.conf import settings
import os

register = template.Library()

@register.filter
def get_product_image(product_name):
    """Map product names to their actual image filenames or return default"""
    image_mapping = {
        # Jewelry
        'Diamond Solitaire Ring': 'uploads/products/diamond-ring.jpg',
        'Pearl Drop Earrings': 'uploads/products/pearl-earrings.jpg', 
        'Rose Gold Tennis Bracelet': 'uploads/products/rose-gold-bracelet.jpg',
        'Emerald Pendant Necklace': 'uploads/products/emerald-necklace.jpg',
        
        # Makeup
        'Luxury Foundation - Ivory': 'uploads/products/foundation-ivory.jpg',
        'Matte Lipstick - Ruby Red': 'uploads/products/lipstick-ruby.jpg',
        'Eyeshadow Palette - Golden Hour': 'uploads/products/eyeshadow-golden.jpg',
        'Anti-Aging Serum': 'uploads/products/anti-aging-serum.jpg',
        'Hydrating Face Mask': 'uploads/products/face-mask.jpg',
        
        # Legacy products (for backward compatibility)
        'Atomic Habits': 'images/products/Atomic_Habits.jpg',
        'The Subtle Art of Not Giving a F*ck': 'images/products/The_Subtle_Art_of_Not_Giving_a_Fuck.jpg',
        'Coiling Dragon': 'images/products/Coiling_Dragon.jpeg',
        'Stellar Transformation': 'images/products/Stellar_Transformation.jpg',
        'How To Win Friends And Influence People': 'images/products/How_To_Win_Friends_And_Influence_People.jpg',
        'Lord of the Mysteries': 'images/products/LOTM.jpg',
        'Circle of Inevitability': 'images/products/COI.jpeg',
        'Embers Ad Infinitum': 'images/products/Embers_Ad_Infinitum.jpeg',
        'Google Pixel': 'images/products/google_pixel.webp',
        'iPhone': 'images/products/iphone.jpg',
    }
    
    # Try to get the mapped image first
    image_path = image_mapping.get(product_name)
    
    if image_path:
        # Check if the file exists
        full_path = os.path.join(settings.BASE_DIR, 'static', image_path)
        media_path = os.path.join(settings.MEDIA_ROOT, image_path.replace('uploads/', ''))
        
        if os.path.exists(full_path):
            return image_path
        elif os.path.exists(media_path):
            return image_path.replace('uploads/', '/media/uploads/')
    
    # Return a default placeholder image
    return 'images/products/placeholder.jpg'

@register.filter
def get_product_media_url(product):
    """Get the media URL for a product's main image"""
    if hasattr(product, 'image') and product.image:
        return product.image.url
    else:
        # Fallback to template tag method
        return get_product_image(product.name)
