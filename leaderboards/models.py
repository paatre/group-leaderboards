from datetime import timedelta
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class BaseActivity(models.Model):
    """
    Represents an activity that can be performed by a user
    for leaderboard purposes. This model is abstract and should
    be inherited by other models that define specific activities
    for various sports and activities.
    """

    activity_date = models.DateField(verbose_name=_("Activity date"))
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="activities",
        verbose_name=_("User"),
    )

    class Meta:
        abstract = True
        ordering = ["-activity_date"]


class RunningActivity(BaseActivity):
    """
    Represents a running activity performed by a user.
    Inherits from BaseActivity to include common fields.
    """

    distance = models.DecimalField(
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Distance"),
    )
    duration = models.DurationField(
        null=True,
        blank=True,
        verbose_name=_("Duration"),
    )
    pace = models.DurationField(
        null=True,
        blank=True,
        verbose_name=_("Pace"),
    )
    heart_rate_avg = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Average heart rate"),
    )
    heart_rate_max = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Maximum heart rate"),
    )
    ascent = models.DecimalField(
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Ascent"),
    )
    descent = models.DecimalField(
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Descent"),
    )

    class Meta(BaseActivity.Meta):
        verbose_name = _("Running activity")
        verbose_name_plural = _("Running activities")

    def __str__(self):
        parts = [
            self.user.username,
            str(self.activity_date) if self.activity_date else None,
            f"{self.distance} km" if self.distance else None,
            str(self.duration) if self.duration else None,
            f"{self.pace}" if self.pace else None,
        ]
        return " - ".join(filter(None, parts))

    def save(self, *args, **kwargs):
        if not self.pace and self.distance and self.duration:
            if self.distance > 0:
                total_seconds = self.duration.total_seconds()
                pace_seconds_per_km = total_seconds / float(self.distance)
                self.pace = timedelta(seconds=round(pace_seconds_per_km))
        super().save(*args, **kwargs)
