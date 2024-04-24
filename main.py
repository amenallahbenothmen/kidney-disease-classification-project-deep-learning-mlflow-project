from CNN_Classifier_Project import logger
from CNN_Classifier_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_Classifier_Project.pipeline.satge_02_prepare_base_model import PrepareBaseModelTrainingPipeline
STAGE_NAME = "DATA Ingestion stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare base model stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
