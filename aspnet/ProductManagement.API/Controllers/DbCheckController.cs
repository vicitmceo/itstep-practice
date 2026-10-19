using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ProductManagement.API.Data;

namespace ProductManagement.API.Controllers;

/// <summary>Перевірка підключення до бази даних.</summary>
[ApiController]
[Route("api/[controller]")]
public class DbCheckController : ControllerBase
{
    private readonly AppDbContext _db;

    public DbCheckController(AppDbContext db) => _db = db;

    [HttpGet]
    public async Task<IActionResult> Check()
    {
        var canConnect = await _db.Database.CanConnectAsync();
        return canConnect
            ? Ok(new { status = "Connected", database = _db.Database.GetDbConnection().Database })
            : StatusCode(503, new { status = "Unavailable" });
    }
}
