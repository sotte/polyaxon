from polyaxon.config_manager import config

PUBLIC_PLUGIN_JOBS = config.get_boolean('POLYAXON_PUBLIC_PLUGIN_JOBS', is_optional=True)
# Roles
ROLE_LABELS_WORKER = config.get_string('POLYAXON_ROLE_LABELS_WORKER')
ROLE_LABELS_DASHBOARD = config.get_string('POLYAXON_ROLE_LABELS_DASHBOARD')
ROLE_LABELS_LOG = config.get_string('POLYAXON_ROLE_LABELS_LOG')
ROLE_LABELS_API = config.get_string('POLYAXON_ROLE_LABELS_API')
K8S_SERVICE_ACCOUNT_NAME = config.get_string('POLYAXON_K8S_SERVICE_ACCOUNT_NAME')
K8S_RBAC_ENABLED = config.get_boolean('POLYAXON_K8S_RBAC_ENABLED')
K8S_PROVISIONER_ENABLED = config.get_boolean('POLYAXON_K8S_PROVISIONER_ENABLED')
K8S_INGRESS_ENABLED = config.get_boolean('POLYAXON_K8S_INGRESS_ENABLED')
K8S_INGRESS_ANNOTATIONS = config.get_string('POLYAXON_K8S_INGRESS_ANNOTATIONS', is_optional=True)
TENSORBOARD_PORT_RANGE = [5700, 6700]
NOTEBOOK_PORT_RANGE = [6700, 7700]

# Types
TYPE_LABELS_CORE = config.get_string('POLYAXON_TYPE_LABELS_CORE')
TYPE_LABELS_EXPERIMENT = config.get_string('POLYAXON_TYPE_LABELS_EXPERIMENT')

# Labels
APP_LABELS_TENSORBOARD = config.get_string('POLYAXON_APP_LABELS_TENSORBOARD')
APP_LABELS_NOTEBOOK = config.get_string('POLYAXON_APP_LABELS_NOTEBOOK')
APP_LABELS_DOCKERIZER = config.get_string('POLYAXON_APP_LABELS_DOCKERIZER')
APP_LABELS_EXPERIMENT = config.get_string('POLYAXON_APP_LABELS_EXPERIMENT')
APP_LABELS_JOB = config.get_string('POLYAXON_APP_LABELS_JOB')

# Selectors
NODE_SELECTORS_EXPERIMENTS = config.get_string(
    'POLYAXON_NODE_SELECTORS_EXPERIMENTS', is_optional=True)
NODE_SELECTORS_CORE = config.get_string(
    'POLYAXON_NODE_SELECTORS_CORE', is_optional=True)

CONTAINER_NAME_EXPERIMENT_JOB = config.get_string('POLYAXON_CONTAINER_NAME_EXPERIMENT_JOB')
CONTAINER_NAME_JOB = config.get_string('POLYAXON_CONTAINER_NAME_JOB')
CONTAINER_NAME_SIDECAR = config.get_string('POLYAXON_CONTAINER_NAME_SIDECAR')
CONTAINER_NAME_INIT = config.get_string('POLYAXON_CONTAINER_NAME_INIT')
CONTAINER_NAME_PLUGIN_JOB = config.get_string('POLYAXON_CONTAINER_NAME_PLUGIN_JOB')
CONTAINER_NAME_DOCKERIZER_JOB = config.get_string('POLYAXON_CONTAINER_NAME_DOCKERIZER_JOB')
JOB_DOCKER_NAME = config.get_string('POLYAXON_JOB_DOCKER_NAME',
                                    is_optional=True,
                                    default='polyaxon/polyaxon-lib')
JOB_SIDECAR_DOCKER_IMAGE = config.get_string('POLYAXON_JOB_SIDECAR_DOCKER_IMAGE')
JOB_INIT_DOCKER_IMAGE = config.get_string('POLYAXON_JOB_INIT_DOCKER_IMAGE',
                                          is_optional=True,
                                          default='ubuntu:16.04')
JOB_DOCKERIZER_IMAGE = config.get_string('POLYAXON_JOB_DOCKERIZER_IMAGE')
TENSORBOARD_DOCKER_IMAGE = config.get_string('POLYAXON_TENSORBOARD_DOCKER_IMAGE',
                                             is_optional=True,
                                             default='tensorflow/tensorflow:1.4.1-py3')
JOB_SIDECAR_LOG_SLEEP_INTERVAL = config.get_int('POLYAXON_JOB_SIDECAR_LOG_SLEEP_INTERVAL',
                                                is_optional=True)
