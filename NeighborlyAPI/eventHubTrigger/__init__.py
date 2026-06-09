import logging
import azure.functions as func

def main(event: func.EventGridEvent):

    logging.info("EVENT GRID TRIGGER FIRED")

    logging.info("Event ID: %s", event.id)

    logging.info("Subject: %s", event.subject)