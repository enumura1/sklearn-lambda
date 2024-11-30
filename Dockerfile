FROM public.ecr.aws/lambda/python:3.12
# Pythonパッケージのインストール
RUN pip install --no-cache-dir \
    scikit-learn \
    numpy \
    scipy
# イメージ内のLAMBDA_TASK_ROOTにapp.pyをコピー
COPY app.py ${LAMBDA_TASK_ROOT}
# Lambdaが実行する関数を指定
CMD [ "app.lambda_handler" ]
