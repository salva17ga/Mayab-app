from django.test import TestCase

# Create your tests here.

from decimal import Decimal
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from apps.portal.models import (
    Mueble,
    Decoracion,
    Arte,
    Exhibicion,
    Interiorismo,
    Foto,
    ruta_foto,
)
### tests covering app models 

class MuebleModelTest(TestCase):
    """Tests para el modelo Mueble."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="usuario_test",
            password="password123",
        )

        self.mueble = Mueble.objects.create(
            Nombre="Mesa de prueba",
            Descripcion="Mesa de madera para testing.",
            Categoria=Mueble.CategoriasMuebles.Mesa,
            Autor="Autor de prueba",
            Precio=Decimal("15000.00"),
            Registrado_por=self.user,
        )

    def test_create_mueble(self):
        """El mueble debe crearse correctamente."""
        self.assertEqual(Mueble.objects.count(), 1)
        self.assertEqual(self.mueble.Nombre, "Mesa de prueba")
        self.assertEqual(
            self.mueble.Categoria,
            Mueble.CategoriasMuebles.Mesa,
        )
        self.assertEqual(self.mueble.Precio, Decimal("15000.00"))

    def test_str(self):
        """__str__ debe devolver el nombre del mueble."""
        self.assertEqual(str(self.mueble), "Mesa de prueba")

    def test_disponible_default(self):
        """Disponible debe ser True por defecto."""
        self.assertTrue(self.mueble.Disponible)

    def test_unique_nombre(self):
        """No deben existir dos muebles con el mismo nombre."""
        with self.assertRaises(IntegrityError):
            Mueble.objects.create(
                Nombre="Mesa de prueba",
                Categoria=Mueble.CategoriasMuebles.Mesa,
                Autor="Otro autor",
                Precio=Decimal("1000.00"),
            )

    def test_descripcion_is_optional(self):
        """La descripción puede omitirse."""
        mueble = Mueble.objects.create(
            Nombre="Silla sin descripción",
            Categoria=Mueble.CategoriasMuebles.Silla_banco,
            Autor="Autor",
            Precio=Decimal("500.00"),
        )

        self.assertIsNone(mueble.Descripcion)

    def test_registered_by_user(self):
        """El mueble puede estar asociado a un usuario."""
        self.assertEqual(self.mueble.Registrado_por, self.user)

    def test_registered_by_user_set_null(self):
        """Al eliminar el usuario, Registrado_por debe quedar en NULL."""
        user_id = self.user.id

        self.user.delete()

        self.mueble.refresh_from_db()

        self.assertIsNone(self.mueble.Registrado_por)


class DecoracionModelTest(TestCase):
    """Tests para el modelo Decoracion."""

    def setUp(self):
        self.decoracion = Decoracion.objects.create(
            Nombre="Espejo de prueba",
            Descripcion="Espejo para testing.",
            Categoria=Decoracion.CategoriasDecoracion.Espejo,
            Autor="Autor de prueba",
            Precio=Decimal("3500.00"),
        )

    def test_create_decoracion(self):
        self.assertEqual(Decoracion.objects.count(), 1)
        self.assertEqual(
            self.decoracion.Nombre,
            "Espejo de prueba",
        )
        self.assertEqual(
            self.decoracion.Categoria,
            Decoracion.CategoriasDecoracion.Espejo,
        )

    def test_str(self):
        self.assertEqual(
            str(self.decoracion),
            "Espejo de prueba",
        )

    def test_disponible_default(self):
        self.assertTrue(self.decoracion.Disponible)

    def test_unique_nombre(self):
        with self.assertRaises(IntegrityError):
            Decoracion.objects.create(
                Nombre="Espejo de prueba",
                Categoria=Decoracion.CategoriasDecoracion.Espejo,
                Autor="Otro autor",
                Precio=Decimal("1000.00"),
            )


class ArteModelTest(TestCase):
    """Tests para el modelo Arte."""

    def setUp(self):
        self.arte = Arte.objects.create(
            Nombre="Pintura de prueba",
            Descripcion="Obra para testing.",
            Categoria=Arte.CategoriasArte.Pintura,
            Autor="Artista de prueba",
            Precio=Decimal("25000.00"),
        )

    def test_create_arte(self):
        self.assertEqual(Arte.objects.count(), 1)
        self.assertEqual(
            self.arte.Nombre,
            "Pintura de prueba",
        )
        self.assertEqual(
            self.arte.Categoria,
            Arte.CategoriasArte.Pintura,
        )

    def test_str(self):
        self.assertEqual(
            str(self.arte),
            "Pintura de prueba",
        )

    def test_disponible_default(self):
        self.assertTrue(self.arte.Disponible)

    def test_unique_nombre(self):
        with self.assertRaises(IntegrityError):
            Arte.objects.create(
                Nombre="Pintura de prueba",
                Categoria=Arte.CategoriasArte.Pintura,
                Autor="Otro artista",
                Precio=Decimal("1000.00"),
            )

    def test_registered_by_user_set_null(self):
        user = User.objects.create_user(
            username="artista_user",
            password="password123",
        )

        arte = Arte.objects.create(
            Nombre="Escultura de prueba",
            Categoria=Arte.CategoriasArte.Escultura,
            Autor="Artista",
            Precio=Decimal("5000.00"),
            Registrado_por=user,
        )

        user.delete()

        arte.refresh_from_db()

        self.assertIsNone(arte.Registrado_por)


class ExhibicionModelTest(TestCase):
    """Tests para el modelo Exhibicion."""

    def setUp(self):
        self.exhibicion = Exhibicion.objects.create(
            Nombre="Exhibición de prueba",
            Autor="Autor de prueba",
            Descripcion="Descripción de la exhibición.",
            Fecha_exhibicion="2026-09-18",
        )

    def test_create_exhibicion(self):
        self.assertEqual(Exhibicion.objects.count(), 1)
        self.assertEqual(
            self.exhibicion.Nombre,
            "Exhibición de prueba",
        )

    def test_str(self):
        self.assertEqual(
            str(self.exhibicion),
            "Exhibición de prueba",
        )

    def test_descripcion_is_optional(self):
        exhibicion = Exhibicion.objects.create(
            Nombre="Exhibición sin descripción",
            Autor="Autor",
            Fecha_exhibicion="2026-09-18",
        )

        self.assertIsNone(exhibicion.Descripcion)

    def test_registered_by_user_set_null(self):
        user = User.objects.create_user(
            username="exhibicion_user",
            password="password123",
        )

        exhibicion = Exhibicion.objects.create(
            Nombre="Exhibición usuario",
            Autor="Autor",
            Fecha_exhibicion="2026-09-18",
            Registrado_por=user,
        )

        user.delete()

        exhibicion.refresh_from_db()

        self.assertIsNone(exhibicion.Registrado_por)


class InteriorismoModelTest(TestCase):
    """Tests para el modelo Interiorismo."""

    def setUp(self):
        self.interiorismo = Interiorismo.objects.create(
            Nombre="Sala de prueba",
            Descripcion="Diseño interior para testing.",
        )

    def test_create_interiorismo(self):
        self.assertEqual(Interiorismo.objects.count(), 1)
        self.assertEqual(
            self.interiorismo.Nombre,
            "Sala de prueba",
        )

    def test_descripcion_is_optional(self):
        interiorismo = Interiorismo.objects.create(
            Nombre="Diseño sin descripción",
        )

        self.assertIsNone(interiorismo.Descripcion)

    def test_registered_by_user_set_null(self):
        user = User.objects.create_user(
            username="interiorismo_user",
            password="password123",
        )

        interiorismo = Interiorismo.objects.create(
            Nombre="Diseño usuario",
            Registrado_por=user,
        )

        user.delete()

        interiorismo.refresh_from_db()

        self.assertIsNone(interiorismo.Registrado_por)


class RutaFotoTest(TestCase):
    """Tests para la función ruta_foto."""

    def setUp(self):
        self.mueble = Mueble.objects.create(
            Nombre="Mesa para foto",
            Categoria=Mueble.CategoriasMuebles.Mesa,
            Autor="Autor",
            Precio=Decimal("1000.00"),
        )

        self.decoracion = Decoracion.objects.create(
            Nombre="Espejo para foto",
            Categoria=Decoracion.CategoriasDecoracion.Espejo,
            Autor="Autor",
            Precio=Decimal("2000.00"),
        )

        self.arte = Arte.objects.create(
            Nombre="Pintura para foto",
            Categoria=Arte.CategoriasArte.Pintura,
            Autor="Autor",
            Precio=Decimal("3000.00"),
        )

        self.exhibicion = Exhibicion.objects.create(
            Nombre="Exhibición para foto",
            Autor="Autor",
            Fecha_exhibicion="2026-09-18",
        )

        self.interiorismo = Interiorismo.objects.create(
            Nombre="Interiorismo para foto",
        )

    def test_mueble_path(self):
        foto = Foto(Mueble=self.mueble)

        path = ruta_foto(foto, "imagen.jpg")

        self.assertEqual(
            path,
            f"productos/muebles/{self.mueble.id}/imagen.jpg",
        )

    def test_decoracion_path(self):
        foto = Foto(Decoracion=self.decoracion)

        path = ruta_foto(foto, "imagen.jpg")

        self.assertEqual(
            path,
            f"productos/decoracion/{self.decoracion.id}/imagen.jpg",
        )

    def test_arte_path(self):
        foto = Foto(Arte=self.arte)

        path = ruta_foto(foto, "imagen.jpg")

        self.assertEqual(
            path,
            f"productos/arte/{self.arte.id}/imagen.jpg",
        )

    def test_exhibicion_path(self):
        foto = Foto(Exhibicion=self.exhibicion)

        path = ruta_foto(foto, "imagen.jpg")

        self.assertEqual(
            path,
            f"exhibicion/{self.exhibicion.id}/imagen.jpg",
        )

    def test_interiorismo_path(self):
        foto = Foto(Interiorismo=self.interiorismo)

        path = ruta_foto(foto, "imagen.jpg")

        self.assertEqual(
            path,
            f"interiorismo/{self.interiorismo.id}/imagen.jpg",
        )


class FotoModelTest(TestCase):
    """Tests para el modelo Foto."""

    def setUp(self):


        self.user = User.objects.create_user(
            username="usuario_test",
            password="password123",
        )

        self.mueble = Mueble.objects.create(
            Nombre="Mueble con foto",
            Categoria=Mueble.CategoriasMuebles.Mesa,
            Autor="Autor",
            Precio=Decimal("10000.00"),
        )

        self.decoracion = Decoracion.objects.create(
            Nombre="Decoración con foto",
            Categoria=Decoracion.CategoriasDecoracion.Espejo,
            Autor="Autor",
            Precio=Decimal("2000.00"),
        )

        self.arte = Arte.objects.create(
            Nombre="Arte con foto",
            Categoria=Arte.CategoriasArte.Pintura,
            Autor="Artista",
            Precio=3000,
        )

        self.exhibicion = Exhibicion.objects.create(
            Nombre="Exhibición con foto",
            Autor="Autor",
            Fecha_exhibicion="2026-09-18",
        )

        self.interiorismo = Interiorismo.objects.create(
            Nombre="Interiorismo con foto",
        )

    def test_foto_can_be_related_to_mueble(self):
        foto = Foto(
            Mueble=self.mueble,
            Imagen="imagen.jpg",
            Registrado_por = self.user
        )

        foto.full_clean()

        self.assertEqual(foto.Mueble, self.mueble)

    def test_foto_can_be_related_to_decoracion(self):
        foto = Foto(
            Decoracion=self.decoracion,
            Imagen="imagen.jpg",
            Registrado_por = self.user
        )

        foto.full_clean()

        self.assertEqual(foto.Decoracion, self.decoracion)

    def test_foto_can_be_related_to_arte(self):
        foto = Foto(
            Arte=self.arte,
            Imagen="imagen.jpg",
            Registrado_por = self.user
        )

        foto.full_clean()

        self.assertEqual(foto.Arte, self.arte)

    def test_foto_can_be_related_to_exhibicion(self):
        foto = Foto(
            Exhibicion=self.exhibicion,
            Imagen="imagen.jpg",
            Registrado_por = self.user
        )

        foto.full_clean()

        self.assertEqual(foto.Exhibicion, self.exhibicion)

    def test_foto_can_be_related_to_interiorismo(self):
        foto = Foto(
            Interiorismo=self.interiorismo,
            Imagen="imagen.jpg",
            Registrado_por = self.user
        )

        foto.full_clean()

        self.assertEqual(
            foto.Interiorismo,
            self.interiorismo,
        )

    def test_foto_cannot_have_multiple_relations(self):
        """Una foto no puede pertenecer a más de una entidad."""

        foto = Foto(
            Mueble=self.mueble,
            Arte=self.arte,
            Imagen="imagen.jpg",
        )

        with self.assertRaises(ValidationError):
            foto.full_clean()

    def test_foto_str_mueble(self):
        foto = Foto(
            Mueble=self.mueble,
            Imagen="imagen.jpg",
        )

        self.assertEqual(
            str(foto),
            "Foto de Mueble con foto - imagen.jpg",
        )

    def test_foto_str_decoracion(self):
        foto = Foto(
            Decoracion=self.decoracion,
            Imagen="imagen.jpg",
        )

        self.assertEqual(
            str(foto),
            "Foto de Decoración con foto - imagen.jpg",
        )

    def test_foto_str_arte(self):
        foto = Foto(
            Arte=self.arte,
            Imagen="imagen.jpg",
        )

        self.assertEqual(
            str(foto),
            "Foto de Arte con foto - imagen.jpg",
        )

    def test_foto_str_interiorismo(self):
        foto = Foto(
            Interiorismo=self.interiorismo,
            Imagen="imagen.jpg",
        )


    def test_foto_cascade_when_mueble_deleted(self):
        """Al eliminar un mueble, sus fotos deben eliminarse."""

        Foto.objects.create(
            Mueble=self.mueble,
            Imagen="imagen.jpg",
        )

        self.assertEqual(Foto.objects.count(), 1)

        self.mueble.delete()

        self.assertEqual(Foto.objects.count(), 0)

    def test_foto_registered_by_user_set_null(self):
        user = User.objects.create_user(
            username="foto_user",
            password="password123",
        )

        foto = Foto.objects.create(
            Mueble=self.mueble,
            Imagen="imagen.jpg",
            Registrado_por=user,
        )

        user.delete()

        foto.refresh_from_db()

        self.assertIsNone(foto.Registrado_por)

