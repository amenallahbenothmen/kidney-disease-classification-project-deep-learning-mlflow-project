from CNN_Classifier_Project.config.configuration import ConfigurationManager
from CNN_Classifier_Project import logger
from CNN_Classifier_Project.components.model_evaluation import Evaluation

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:

  def __init__(self):
    pass
  def main(self):
    config= ConfigurationManager()
    eval_config=config.get_evaluation_config()
    evaluation=Evaluation(config=eval_config)
    evaluation.evaluation()
    evaluation.log_into_mlflow()
  
  
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model = EvaluationPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e 