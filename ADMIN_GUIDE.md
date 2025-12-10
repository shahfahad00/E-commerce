# Admin Panel Guide - Product Management

## Access the Admin Panel

1. **Local Development:**
   - URL: http://localhost:8000/admin
   - Username: fahad
   - Password: 123

2. **Production (Render):**
   - URL: https://your-app.onrender.com/admin
   - Same credentials

## Adding Products

### Method 1: Through Admin Panel (Manual)

1. Go to http://localhost:8000/admin
2. Click on "Products" under CATALOG section
3. Click "Add Product" button
4. Fill in the form:
   - **Name**: Product name (e.g., "iPhone 15")
   - **Slug**: Auto-generated from name (or customize)
   - **Description**: Detailed product description
   - **Category**: Select from dropdown
   - **Price**: Product price
   - **Stock**: Available quantity
   - **Available**: Check to make product visible
   - **Image URL**: Paste image URL (recommended) OR
   - **Image**: Upload image file
5. Click "Save"

### Method 2: Bulk Load via Management Command

We've created sample products for you! To load more:

```bash
python manage.py load_sample_products
```

### Method 3: Create Custom Products via Command

Edit `catalog/management/commands/load_sample_products.py` and add your products to the list:

```python
{
    'name': 'Your Product Name',
    'slug': 'your-product-name',
    'description': 'Product description here',
    'price': 99.99,
    'category': electronics,  # or clothing, books, etc.
    'stock': 50,
    'image_url': 'https://example.com/image.jpg'
}
```

Then run: `python manage.py load_sample_products`

## Image Options

### Option 1: Image URLs (Recommended for Production)

Use free image sources:
- **Unsplash**: https://unsplash.com (free high-quality images)
- **Pexels**: https://pexels.com (free stock photos)
- **Pixabay**: https://pixabay.com (free images)

To get Unsplash image URL:
1. Go to unsplash.com
2. Search for product type (e.g., "laptop")
3. Click on image
4. Right-click > Copy image address
5. Paste into "Image URL" field in admin

### Option 2: Upload Files (For Local Development)

1. In admin panel, click "Choose File" under Image section
2. Select image from your computer
3. Images will be stored in `/media/products/` folder

**Note:** For production on Render (free tier), use Image URLs instead of file uploads, as the file system is ephemeral.

## Managing Categories

1. Go to http://localhost:8000/admin
2. Click on "Categories" under CATALOG section
3. Click "Add Category"
4. Fill in:
   - **Name**: Category name
   - **Slug**: Auto-generated from name
   - **Description**: Category description
5. Click "Save"

## Current Sample Data

We've already loaded:
- **Categories**: Electronics, Clothing, Books
- **Products**: 6 sample products with images

## Tips

1. **Image URLs** are better for production deployment
2. **Slugs** should be URL-friendly (lowercase, hyphens)
3. Use **Stock** field to track inventory
4. Uncheck **Available** to hide products without deleting them
5. You can **bulk edit** price, stock, and availability from the product list

## API Access

Your products are available via API:
- All products: http://localhost:8000/api/products/
- Single product: http://localhost:8000/api/products/{id}/
- Categories: http://localhost:8000/api/categories/

## Next Steps

1. Access admin panel: http://localhost:8000/admin
2. View your products
3. Add more products or edit existing ones
4. Test the API endpoints
