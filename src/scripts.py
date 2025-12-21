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



# import os
# import cv2
# from pathlib import Path

# # Hàm resize ảnh sử dụng OpenCV
# def resize_images_opencv(input_dir, output_dir, size=(224, 224)):
#     """
#     Resize toàn bộ ảnh trong input_dir → output_dir theo cấu trúc thư mục con,
#     sử dụng OpenCV.

#     input_dir/
#         ├── cars/
#         ├── trucks/
#         ├── others/
#         ├── motorbikes/
#         ├── bus/
#         └── bicycles/

#     output_dir/
#         ├── cars/
#         ├── trucks/
#         ├── others/
#         ├── motorbikes/
#         ├── bus/
#         └── bicycles/
#     """
    
#     input_dir = Path(input_dir)
#     output_dir = Path(output_dir)
#     output_dir.mkdir(parents=True, exist_ok=True)

#     supported_ext = (".jpg", ".jpeg", ".png")

#     # Duyệt qua từng thư mục con
#     for class_folder in os.listdir(input_dir):
#         class_path = input_dir / class_folder

#         # Bỏ qua nếu không phải thư mục
#         if not class_path.is_dir():
#             continue

#         # Tạo thư mục tương ứng trong output
#         output_class_dir = output_dir / class_folder
#         output_class_dir.mkdir(parents=True, exist_ok=True)

#         # Duyệt ảnh trong thư mục lớp
#         for filename in os.listdir(class_path):
#             if not filename.lower().endswith(supported_ext):
#                 continue

#             img_path = class_path / filename
#             img = cv2.imread(str(img_path))
#             if img is None:
#                 continue

#             # Resize về (224 x 224)
#             img_resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

#             # Lưu ảnh giữ nguyên tên + thư mục lớp
#             save_path = output_class_dir / filename
#             cv2.imwrite(str(save_path), img_resized)

#     print(f"Resize done: {output_dir}")

#làm nét ảnh
import cv2
import os
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

def unsharp_masking_process(image_info):
    """
    Xử lý làm nét và lưu ảnh vào đúng cấu trúc thư mục con.
    """
    input_path, output_path = image_info
    try:
        # Đảm bảo thư mục con ở đầu ra đã tồn tại
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        img = cv2.imread(str(input_path))
        if img is None: return False
        
        # Thuật toán USM
        blurred = cv2.GaussianBlur(img, (0, 0), sigmaX=2.0)
        sharpened = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)

        # Lưu ảnh
        cv2.imwrite(str(output_path), sharpened, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
        return True
    except Exception as e:
        print(f"Lỗi tại {input_path}: {e}")
        return False

if __name__ == '__main__':
    # --- CẤU HÌNH ĐƯỜNG DẪN ---
    input_root = Path('data/processed')           # Thư mục gốc chứa 6 thư mục con
    output_root = Path('process_sharpened') # Thư mục gốc đầu ra
    # --------------------------

    # Lấy toàn bộ đường dẫn ảnh trong tất cả các thư mục con (Recursive)
    extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    
    tasks = []
    # rglob('*') giúp tìm kiếm xuyên suốt các thư mục con
    for img_path in input_root.rglob('*'):
        if img_path.suffix.lower() in extensions:
            # Tính toán đường dẫn tương đối để tái tạo cấu trúc ở thư mục đích
            relative_path = img_path.relative_to(input_root)
            target_path = output_root / relative_path
            tasks.append((img_path, target_path))

    print(f"Tìm thấy {len(tasks)} ảnh trong {len(next(os.walk(input_root))[1])} thư mục con.")
    
    start_time = time.time()

    # Chạy đa nhân CPU
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(unsharp_masking_process, tasks))

    print(f"\nHoàn thành!")
    print(f"Thời gian: {time.time() - start_time:.2f} giây.")
    print(f"Cấu trúc thư mục đã được bảo toàn tại: {output_root.absolute()}")