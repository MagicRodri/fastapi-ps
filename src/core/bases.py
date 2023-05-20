# Models import prio to alembic import
from db.base import Base  # noqa
from quizzes.models import *  # noqa
from users.models import *  # noqa
