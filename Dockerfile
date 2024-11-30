FROM public.ecr.aws/lambda/python:3.12
RUN pip install --no-cache-dir \
    scikit-learn \
    numpy \
    scipy

COPY app.py ${LAMBDA_TASK_ROOT}
CMD [ "app.lambda_handler" ]
