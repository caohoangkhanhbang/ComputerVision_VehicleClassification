#THỊ GIÁC MÁY TÍNH VÀ NHẬN DẠNG MẪU

#PHÂN LOẠI PHƯƠNG TIỆN GIAO THÔNG ĐƯỜNG BỘ TẠI VIỆT NAM


# ComputerVision_VehicleClassification
#Thành viên nhóm
<h3>
1. Nguyễn Lê Quỳnh Như – 1001250016<br/>
2. Phan Trần Minh Tâm - 1001250019<br/>
3. Nguyễn Minh Trí – 1001250032<br/>
4. Cao Hoàng Khánh Băng - 1001250006
</h3>

<h2>Lý do lựa chọn đề tài</h2>
<p>
  Giao thông đường bộ tại Việt Nam đang đối mặt với nhiều thách thức do tốc độ đô thị hóa nhanh, mật độ phương tiện cao và sự đa dạng về loại hình phương tiện, đặc biệt là tỷ lệ xe máy chiếm ưu thế. Việc quản lý và giám sát giao thông theo phương pháp thủ công hoặc bán tự động hiện nay còn gặp nhiều hạn chế về độ chính xác, chi phí và khả năng mở rộng.
Trong bối cảnh đó, thị giác máy tính (Computer Vision) đóng vai trò quan trọng trong việc xây dựng các hệ thống giao thông thông minh, cho phép máy tính tự động phân tích hình ảnh và video để nhận diện, phân loại và thống kê phương tiện giao thông. Ứng dụng Computer Vision giúp nâng cao hiệu quả giám sát, hỗ trợ điều tiết giao thông và cung cấp dữ liệu phục vụ phân tích, ra quyết định.
</p>

<h2>Đối tượng và phạm vi nghiên cứu</h2>
<p>
  Đối tượng nghiên cứu của đề tài là các ảnh tĩnh, trong đó mỗi ảnh chỉ chứa một phương tiện giao thông đường bộ. Các phương tiện được phân chia thành sáu lớp, bao gồm: xe máy, ô tô, xe buýt, xe tải, xe đạp và các phương tiện khác.
Phạm vi nghiên cứu của đề tài được giới hạn ở bài toán phân loại ảnh (image classification) trong lĩnh vực thị giác máy tính. Đề tài không xem xét các bài toán liên quan như phát hiện đối tượng, theo dõi phương tiện hay nhận dạng biển số. Các thí nghiệm được thực hiện trong môi trường thử nghiệm nhằm đánh giá hiệu quả của mô hình và phương pháp đề xuất. 
</p>

## Cấu trúc dự án (Project Structure)

```text
project/
├── configs/                    # Cấu hình (model, training, augmentation...)
│   ├── config.yaml
│   └── model_config.yaml
│
├── data/                       # Dữ liệu theo chuẩn ImageFolder
├── raw/                        # Ảnh gốc
│   │   ├── class1/
│   │   ├── class2/
│   │   └── ...
├── processed/                  #Ảnh đã tiền xử lý xong
│   │   ├── class1/
│   │   ├── class2/
│   │  
├── train/
│   │   ├── class1/
│   │   ├── class2/
│   │   └── ...
│   ├── val/
│   └── test/
│
├── src/
│   ├── datasets/
│   │   └── dataset.py          # DataLoader, transform, augmentation
│   ├── script.py               # Script tiền xử lý ảnh
│   ├── model.py                # Model lựa chọn để xử lý EfficientNet-V2
│   ├── train.py                # Vòng lặp training chính
│   ├── eval.py                 # Đánh giá model (accuracy, F1)
│   ├── inference.py            # Dự đoán ảnh đơn lẻ
│   ├── utils.py                # Tiện ích: seed, logger, metrics
│   └── transforms.py           # Tập trung các augment (ColorJitter, Blur, Resize)
│
├── outputs/                    # Lưu kết quả training
│   ├── checkpoints/
│   │   └── best_model.pth
│   └── logs/
│       └── training_log.txt
│
├── requirements.txt            # Danh sách thư viện
├── README.md                   # Hướng dẫn chạy dự án
└── .gitignore

Lệnh chạy resize ảnh:
python -c "from src.scripts import resize_images_opencv; resize_images_opencv('data/raw','data/processed',(224,224))"

```



