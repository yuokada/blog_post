package controllers

import play.api._
import play.api.mvc._
import play.api.libs.json.Json

object Application extends Controller {

  def index = Action {
    val fblist = Range(1, 30).map(x => mapFizzBuzz(x)).toList
    val rset = Map("ResultSet"->Map("Result"->fblist))
    Ok(Json.toJson(rset))
    // Ok(Json.toJson("Hello World"))
    // Redirect(routes.Application.tasks)
  }

  def windex = Action {
    val ls = 1 to 100
    val fblist = Range(1, 30).map(x => mapFizzBuzz(x)).toList
    val rset = Map("ResultSet"->Map("Result"->fblist))
    Ok(Json.toJson(rset))
    // Ok(Json.toJson("Hello World"))
    // Redirect(routes.Application.tasks)
  }

  def sayHello() = Action { implicit request =>
    val dom = request().body().asXml();
    if(dom == null) {
      return badRequest("Expecting Xml data");
    } else {
      String name = XPath.selectText("//name", dom);
      if(name == null) {
        return badRequest("Missing parameter [name]");
      } else {
        return ok("Hello " + name);
      }
    }
  }

  def hello = Action {
    Ok(views.html.index("Your new application is ready."))
  }

  def mapFizzBuzz(x:Int): String = {
    x match {
      case x if x % 15 == 0 => "FizzBuzz"
      case x if x % 5  == 0 => "Buzz"
      case x if x % 3 == 0  => "Fizz"
      case _                => x.toString
    }
  }

}
