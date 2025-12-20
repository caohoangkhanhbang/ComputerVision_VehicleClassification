## Cấu trúc dự án (Project Structure)

```text
project/
├── configs/                    # Cấu hình (model, training, augmentation...)
│   ├── config.yaml
│   └── model_config.yaml
│
├── data/                       # Dữ liệu theo chuẩn ImageFolder
│   ├── train/
│   │   ├── class1/
│   │   ├── class2/
│   │   └── ...
│   ├── val/
│   └── test/
│
├── src/
│   ├── datasets/
│   │   └── dataset.py          # DataLoader, transform, augmentation
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
├── scripts/                    # Chứa các script xử lý ảnh
│   ├── resize_images.py        # Script tiền xử lý resize 384x384
│   ├── remove_duplicates.py    # Script lọc ảnh trùng
│   └── clean_blurry_images.py  # Script loại ảnh mờ
│
├── requirements.txt            # Danh sách thư viện
├── README.md                   # Hướng dẫn chạy dự án
└── .gitignore




# ComputerVision_VehicleClassification
#Thành viên nhóm
<h3>
1. Nguyễn Lê Quỳnh Như – 1001250016<br/>
2. Phan Trần Minh Tâm - 1001250019<br/>
3. Nguyễn Minh Trí – 1001250032<br/>
4. Cao Hoàng Khánh Băng - 1001250006
</h3>


