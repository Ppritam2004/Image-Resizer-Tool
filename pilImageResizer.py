{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5e4a8a1d-05ab-40ae-83bf-766e1030e8d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: Pillow in c:\\users\\prita\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (11.2.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install Pillow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a8e127e2-f1c4-4e8e-94e3-6a9a28349f66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "✨ 0 image(s) resized and saved in 'resized/'\n",
      "📦 Zip file created: resized_images.zip\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "from PIL import Image\n",
    "import shutil\n",
    "\n",
    "# Folder settings\n",
    "input_folder = 'images'\n",
    "output_folder = 'resized'\n",
    "new_size = (800, 800)  # Width x Height\n",
    "output_format = 'JPEG'  # Change to 'PNG' or 'WEBP' if needed\n",
    "\n",
    "# Create output folder if it doesn't exist\n",
    "os.makedirs(output_folder, exist_ok=True)\n",
    "\n",
    "# Resize and save images\n",
    "count = 0\n",
    "for filename in os.listdir(input_folder):\n",
    "    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.jfif')):\n",
    "        input_path = os.path.join(input_folder, filename)\n",
    "        output_name = os.path.splitext(filename)[0] + '.jpg'\n",
    "        output_path = os.path.join(output_folder, output_name)\n",
    "\n",
    "        try:\n",
    "            with Image.open(input_path) as img:\n",
    "                img = img.resize(new_size, Image.ANTIALIAS)\n",
    "                img.convert('RGB').save(output_path, output_format)\n",
    "                print(f\"✅ Saved: {output_path}\")\n",
    "                count += 1\n",
    "        except Exception as e:\n",
    "            print(f\"❌ Error processing {filename}: {e}\")\n",
    "\n",
    "# Create zip archive of resized folder\n",
    "zip_filename = 'resized_images.zip'\n",
    "shutil.make_archive('resized_images', 'zip', output_folder)\n",
    "\n",
    "print(f\"\\n✨ {count} image(s) resized and saved in '{output_folder}/'\")\n",
    "print(f\"📦 Zip file created: {zip_filename}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "3530595e-a8d9-4176-a8b2-06dbd0daab39",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Files inside 'images/' folder:\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "print(\"Files inside 'images/' folder:\")\n",
    "for f in os.listdir('images'):\n",
    "    print(\"📄\", f)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "db32e8da-7c5c-46c6-8111-bfca1224c1ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f07c84a7f7644e9fb327d473be4ac70d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FileUpload(value=(), accept='image/*', description='Upload', multiple=True)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import os\n",
    "from PIL import Image\n",
    "from ipywidgets import FileUpload\n",
    "from IPython.display import display\n",
    "import shutil\n",
    "\n",
    "# Step 1: Upload Widget\n",
    "upload_widget = FileUpload(accept='image/*', multiple=True)\n",
    "display(upload_widget)\n",
    "\n",
    "# Step 2: Wait for user to upload manually, then run below after uploading\n",
    "def process_upload_resize_zip(widget):\n",
    "    # Create folders\n",
    "    input_folder = 'images'\n",
    "    output_folder = 'resized'\n",
    "    os.makedirs(input_folder, exist_ok=True)\n",
    "    os.makedirs(output_folder, exist_ok=True)\n",
    "\n",
    "    # Save uploaded images\n",
    "    if widget.value:\n",
    "        for file in widget.value:\n",
    "            filename = file['name']\n",
    "            content = file['content']\n",
    "            with open(os.path.join(input_folder, filename), 'wb') as f:\n",
    "                f.write(content)\n",
    "        print(f\"✅ Saved {len(widget.value)} image(s) to '{input_folder}/'\")\n",
    "    else:\n",
    "        print(\"⚠️ No files were uploaded.\")\n",
    "        return\n",
    "\n",
    "    # Resize images\n",
    "    new_size = (800, 800)\n",
    "    output_format = 'JPEG'\n",
    "    count = 0\n",
    "\n",
    "    for filename in os.listdir(input_folder):\n",
    "        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.jfif')):\n",
    "            input_path = os.path.join(input_folder, filename)\n",
    "            output_name = os.path.splitext(filename)[0] + '.jpg'\n",
    "            output_path = os.path.join(output_folder, output_name)\n",
    "            try:\n",
    "                with Image.open(input_path) as img:\n",
    "                    img = img.resize(new_size, Image.ANTIALIAS)\n",
    "                    img.convert('RGB').save(output_path, output_format)\n",
    "                    count += 1\n",
    "            except Exception as e:\n",
    "                print(f\"❌ Failed: {filename} | Error: {e}\")\n",
    "\n",
    "    print(f\"✅ {count} image(s) resized and saved in '{output_folder}/'\")\n",
    "\n",
    "    # Zip the output folder\n",
    "    zip_filename = 'resized_images.zip'\n",
    "    shutil.make_archive('resized_images', 'zip', output_folder)\n",
    "    print(f\"📦 Zip file created: {zip_filename}\\nYou can download it from the file browser panel.\")\n",
    "\n",
    "# ✨ Step 3: Manually call this AFTER uploading images\n",
    "# process_upload_resize_zip(upload_widget)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74ddccc5-08a5-400b-9e06-094809a8816f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
