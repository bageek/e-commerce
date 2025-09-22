from django.core.management.base import BaseCommand
from store.models import Category, Product
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Create sample luxury jewelry and makeup data'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            'Rings',
            'Necklaces', 
            'Earrings',
            'Bracelets',
            'Foundation',
            'Lipstick', 
            'Eyeshadow',
            'Skincare'
        ]
        
        created_categories = {}
        for cat_name in categories_data:
            category, created = Category.objects.get_or_create(name=cat_name)
            created_categories[cat_name] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {cat_name}'))
                
        # Create sample products
        products_data = [
            # Jewelry
            {
                'name': 'Diamond Solitaire Ring',
                'category': 'Rings',
                'price': '2999.99',
                'description': 'Exquisite 1-carat diamond solitaire ring set in 18k white gold. Perfect for engagements or special occasions.',
                'material': '18k White Gold',
                'carat': '1.00',
                'gemstone': 'Diamond',
                'color': 'White',
                'size': '6',
                'featured': True,
                'in_stock': True,
                'image': 'uploads/products/diamond-ring.jpg'
            },
            {
                'name': 'Pearl Drop Earrings',
                'category': 'Earrings', 
                'price': '499.99',
                'description': 'Classic freshwater pearl drop earrings with 14k gold findings. Timeless elegance for any occasion.',
                'material': '14k Gold',
                'gemstone': 'Freshwater Pearl',
                'color': 'White',
                'featured': True,
                'in_stock': True,
                'image': 'uploads/products/pearl-earrings.jpg'
            },
            {
                'name': 'Rose Gold Tennis Bracelet',
                'category': 'Bracelets',
                'price': '1299.99', 
                'description': 'Stunning tennis bracelet featuring premium cubic zirconia stones set in rose gold.',
                'material': '14k Rose Gold',
                'color': 'Rose Gold',
                'size': '7 inches',
                'featured': True,
                'in_stock': True,
                'image': 'uploads/products/rose-gold-bracelet.jpg'
            },
            {
                'name': 'Emerald Pendant Necklace',
                'category': 'Necklaces',
                'price': '899.99',
                'description': 'Beautiful emerald pendant necklace with delicate gold chain. A perfect statement piece.',
                'material': '14k Yellow Gold', 
                'gemstone': 'Emerald',
                'color': 'Green',
                'size': '18 inches',
                'in_stock': True,
                'image': 'uploads/products/emerald-necklace.jpg'
            },
            
            # Makeup
            {
                'name': 'Luxury Foundation - Ivory',
                'category': 'Foundation',
                'price': '89.99',
                'description': 'Premium long-wear foundation with buildable coverage. Suitable for all skin types.',
                'brand': 'LuxeBeauty Pro',
                'shade': 'Ivory',
                'skin_type': 'All',
                'color': 'Ivory',
                'size': '30ml',
                'featured': True,
                'in_stock': True,
                'image': 'uploads/products/foundation-ivory.jpg'
            },
            {
                'name': 'Matte Lipstick - Ruby Red',
                'category': 'Lipstick',
                'price': '45.99',
                'description': 'Rich, long-lasting matte lipstick in a stunning ruby red shade. Cruelty-free formula.',
                'brand': 'LuxeBeauty',
                'shade': 'Ruby Red',
                'skin_type': 'All',
                'color': 'Red',
                'size': '4g',
                'featured': True,
                'in_stock': True,
                'is_sale': True,
                'sale_price': '35.99',
                'image': 'uploads/products/lipstick-ruby.jpg'
            },
            {
                'name': 'Eyeshadow Palette - Golden Hour',
                'category': 'Eyeshadow',
                'price': '79.99',
                'description': '12-shade eyeshadow palette featuring warm golden and bronze tones. Highly pigmented and blendable.',
                'brand': 'LuxeBeauty Pro',
                'shade': 'Golden Hour',
                'skin_type': 'All',
                'color': 'Multi',
                'size': 'Standard',
                'featured': True,
                'in_stock': True,
                'image': 'uploads/products/eyeshadow-golden.jpg'
            },
            {
                'name': 'Anti-Aging Serum',
                'category': 'Skincare',
                'price': '129.99',
                'description': 'Advanced anti-aging serum with retinol and vitamin C. Reduces fine lines and improves skin texture.',
                'brand': 'LuxeBeauty Skin',
                'skin_type': 'Mature',
                'size': '30ml',
                'in_stock': True,
                'image': 'uploads/products/anti-aging-serum.jpg'
            },
            {
                'name': 'Hydrating Face Mask',
                'category': 'Skincare',
                'price': '39.99',
                'description': 'Luxurious hydrating face mask with hyaluronic acid and natural botanicals.',
                'brand': 'LuxeBeauty Skin',
                'skin_type': 'Dry',
                'size': '100ml',
                'in_stock': True,
                'image': 'uploads/products/face-mask.jpg'
            }
        ]
        
        for product_data in products_data:
            category_name = product_data.pop('category')
            category = created_categories[category_name]
            
            # Create slug from name
            product_data['slug'] = slugify(product_data['name'])
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={**product_data, 'category': category}
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))
        
        self.stdout.write(self.style.SUCCESS('Sample data creation completed!'))