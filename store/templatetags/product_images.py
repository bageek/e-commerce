from django import template

register = template.Library()

@register.filter
def get_product_image(product_name):
    """Map product names to their actual image filenames"""
    image_mapping = {
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
    return image_mapping.get(product_name, 'images/products/Atomic_Habits.jpg')
