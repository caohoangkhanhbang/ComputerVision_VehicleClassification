# import os
# import cv2
# from pathlib import Path

# def resize_images_opencv(input_dir, output_dir, size=(224, 224)):
#     """
#     Resize toàn bộ ảnh trong input_dir → output_dir bằng OpenCV.
    
#     Args:
#         input_dir (str): đường dẫn folder chứa ảnh gốc.
#         output_dir (str): đường dẫn folder lưu ảnh đã resize.
#         size (tuple): kích thước resize (default = 224x224).
#     """
    
#     input_dir = 'data/raw'
#     output_dir = 'data/processed'
#     output_dir.mkdir(parents=True, exist_ok=True)

#     supported_ext = (".jpg", ".jpeg", ".png")

#     for filename in os.listdir(input_dir):
#         if not filename.lower().endswith(supported_ext):
#             continue

#         img_path = input_dir / filename
#         img = cv2.imread(str(img_path))
#         if img is None:
#             continue

#         # Resize về (224 x 224)
#         img_resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

#         # Lưu ảnh
#         save_path = output_dir / filename
#         cv2.imwrite(str(save_path), img_resized)

#     print(f"[INFO] Resize xong. Ảnh đã lưu tại: {output_dir}")



import os
import cv2
from pathlib import Path

# Hàm resize ảnh sử dụng OpenCV
def resize_images_opencv(input_dir, output_dir, size=(224, 224)):
    """
    Resize toàn bộ ảnh trong input_dir → output_dir theo cấu trúc thư mục con,
    sử dụng OpenCV.

    input_dir/
        ├── cars/
        ├── trucks/
        ├── others/
        ├── motorbikes/
        ├── bus/
        └── bicycles/

    output_dir/
        ├── cars/
        ├── trucks/
        ├── others/
        ├── motorbikes/
        ├── bus/
        └── bicycles/
    """
    
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    supported_ext = (".jpg", ".jpeg", ".png")

    # Duyệt qua từng thư mục con
    for class_folder in os.listdir(input_dir):
        class_path = input_dir / class_folder

        # Bỏ qua nếu không phải thư mục
        if not class_path.is_dir():
            continue

        # Tạo thư mục tương ứng trong output
        output_class_dir = output_dir / class_folder
        output_class_dir.mkdir(parents=True, exist_ok=True)

        # Duyệt ảnh trong thư mục lớp
        for filename in os.listdir(class_path):
            if not filename.lower().endswith(supported_ext):
                continue

            img_path = class_path / filename
            img = cv2.imread(str(img_path))
            if img is None:
                continue

            # Resize về (224 x 224)
            img_resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

            # Lưu ảnh giữ nguyên tên + thư mục lớp
            save_path = output_class_dir / filename
            cv2.imwrite(str(save_path), img_resized)

    print(f"Resize done: {output_dir}")
