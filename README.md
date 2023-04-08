# Vertex-AI
Vertex AI is a machine learning (ML) platform that lets you train and deploy ML models and AI applications. 

Youtub video link : https://www.youtube.com/watch?v=oeRn13i28DE

Vertex AI provides several options for model training:
1. AutoML lets you train tabular, image, text, or video data without writing code or preparing data splits.
2. Custom training gives you complete control over the training process, including using your preferred ML framework, writing your own training code, and choosing hyperparameter tuning options.

Steps to create a AutoML training pipeline
1. Data creation: Upload your image dataset into bucket.
2. Data labeling: Convert annotation into Vertex AI format: 
   1. Dataset_type, GS-URL, class_name, X_MIN,Y_MIN,X_MAX,Y_MIN, X_MAX,Y_MAX,X_MIN,Y_MAX. 
   2. If you have labels in yolov5 csv formats run this file -> convert_yolov5_labels_to_vertex_ai_format.py.
3. Selete AutoMl option and start training.

Steps to create a custom training pipeline
1. Data creation: Upload your image dataset into bucket.
2. Data labeling: Convert annotation into Vertex AI format: 
   1. Dataset_type, GS-URL, class_name, X_MIN,Y_MIN,X_MAX,Y_MIN, X_MAX,Y_MAX,X_MIN,Y_MAX. 
   2. If you have labels in yolov5 csv formats run this file -> convert_yolov5_labels_to_vertex_ai_format.py.
3. Build and deploy Docker Image.
   1. Run 'install_gcloud.sh' on terminal.
   2. Edit tasks.py & new_coco128.yaml.
   3. Run 'gcloud builds submit --tag gcr.io/[Project_id]/image-name --timeout=3600 .'
4. Select custom training option, select container image, instance and start training.
 