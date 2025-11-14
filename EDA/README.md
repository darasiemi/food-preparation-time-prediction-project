# ml-zoomcamp-project

To create project environment
```bash
conda create -n ml-zc-project python=3.11
```

To activate environment
```bash
conda activate ml-zc-project
```

To install libraries
```bash
conda install numpy pandas scikit-learn seaborn jupyter
```

To install kaggle
```bash
conda install -c conda-forge kaggle
```

```bash
mkdir -p ~/.kaggle
mv kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

To download dataset

```bash
kaggle datasets download ahsan81/food-ordering-and-delivery-app-dataset
```

To unzip
```bash
unzip "food-ordering-and-delivery-app-dataset.zip" -d "data/"
```

To launch jupyter notebook
```bash
jupyter notebook
```





