import mill._, scalalib._
import ammonite.ops._
import java.nio.file.Paths

object knitkit extends ScalaModule {
  def scalaVersion = "2.13.6"

  def millSourcePath = super.millSourcePath / ammonite.ops.up

  def unmanagedClasspath = T {
    val lib_path = T.ctx.env.get("MILL_LIB") match {
      case Some(lib) => Path(Paths.get(lib).toAbsolutePath)
      case None      => millSourcePath / "lib"
    }
    if (!ammonite.ops.exists(lib_path)) Agg()
    else Agg.from(ammonite.ops.ls(lib_path).map(PathRef(_)))
  }
}
