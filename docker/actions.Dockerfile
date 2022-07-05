FROM rasa/rasa-sdk:3.0.6

WORKDIR /rasa_vn_core
COPY ./bot /bot

USER root
RUN apt update && apt install make
USER 1001

ENTRYPOINT []
CMD []