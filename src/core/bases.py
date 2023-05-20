# Models import prio to alembic import
from db.base import Base  # noqa
from quizzes.models import Quiz  # noqa
from users.models import User  # noqa
