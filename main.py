import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def main():
    # 1. Створення даних (Create)
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")

    Actor.objects.create(first_name="George", last_name="Clooney")
    Actor.objects.create(first_name="Keanu", last_name="Reeves")
    Actor.objects.create(first_name="Scarlett", last_name="Keagan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # 2. Оновлення даних (Update)
    Genre.objects.filter(name="Drama").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Clooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Keanu", last_name="Reeves").update(first_name="Keanu", last_name="Reeves")

    # 3. Видалення даних (Delete)
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. Повернення відфільтрованого та відсортованого QuerySet
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
