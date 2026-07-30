from decimal import Decimal
from django.utils import timezone
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from subscriptions.models import ProductVariant, Promotion, PromotionRedemption, Subscription


class CommercialPricingService:
    @staticmethod
    def calculate_school_price(stream_count: int, subject_count: int) -> dict:
        """
        Calculates school term subscription price according to approved stakeholder rules:
          1 stream  -> KES 1,000
          2 streams -> KES 1,300
          3 streams -> KES 1,600
          4 streams -> KES 1,900
          Rule: KES 1,000 base + KES 300 per additional stream.
          Total = per_subject_price * subject_count
        """
        if stream_count < 1:
            raise ValidationError("At least one stream must be selected.")
        if subject_count < 1:
            raise ValidationError("At least one subject must be selected.")

        per_subject_price = Decimal(1000) + Decimal(stream_count - 1) * Decimal(300)
        total_price = per_subject_price * Decimal(subject_count)

        return {
            "stream_count": stream_count,
            "subject_count": subject_count,
            "per_subject_price": per_subject_price,
            "total_price": total_price,
            "currency": "KES"
        }

    @staticmethod
    def evaluate_promotion_eligibility(user, variant: ProductVariant, promotion_id=None, coupon_code=None):
        """
        Evaluates eligibility for a promotion on a given product variant.
        Returns tuple of (Promotion or None, final_price Decimal).
        """
        now = timezone.now()
        promo = None

        if promotion_id:
            promo = Promotion.objects.filter(id=promotion_id, is_active=True).first()
        elif coupon_code:
            promo = Promotion.objects.filter(code=coupon_code, is_active=True).first()
        else:
            promo = Promotion.objects.filter(
                product_variant=variant,
                is_active=True,
                start_date__lte=now
            ).filter(Q(end_date__isnull=True) | Q(end_date__gte=now)).first()

        if not promo:
            return None, variant.price

        if promo.product_variant_id != variant.id:
            return None, variant.price

        # Check redemption limit per user
        user_redemptions = PromotionRedemption.objects.filter(user=user, promotion=promo).count()
        if user_redemptions >= promo.max_redemptions_per_user:
            return None, variant.price

        # Evaluate rule_type
        if promo.rule_type == "FIRST_PURCHASE":
            has_prev_sub = Subscription.objects.filter(
                user=user,
                product_variant__product=variant.product,
                status_state__in=["ACTIVE", "EXPIRED"]
            ).exists()
            if has_prev_sub:
                return None, variant.price

        return promo, promo.promotional_price
