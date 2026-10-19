using AutoMapper;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ProductManagement.API.Data;
using ProductManagement.API.DTOs;
using ProductManagement.API.Models;

namespace ProductManagement.API.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ClientsController : ControllerBase
{
    private readonly AppDbContext _db;
    private readonly IMapper _mapper;

    public ClientsController(AppDbContext db, IMapper mapper)
    {
        _db = db;
        _mapper = mapper;
    }

    // GET /api/clients: список клієнтів (DTO без Phone)
    [HttpGet]
    public async Task<ActionResult<IEnumerable<ClientDto>>> GetAll()
    {
        var clients = await _db.Clients.AsNoTracking().OrderBy(c => c.Id).ToListAsync();
        return Ok(_mapper.Map<List<ClientDto>>(clients));
    }

    [HttpGet("{id:int}")]
    public async Task<ActionResult<ClientDto>> GetById(int id)
    {
        var client = await _db.Clients.AsNoTracking().FirstOrDefaultAsync(c => c.Id == id);
        return client is null ? NotFound() : Ok(_mapper.Map<ClientDto>(client));
    }

    // POST /api/clients: 201 Created і новий Id
    [HttpPost]
    public async Task<ActionResult<ClientDto>> Create(CreateClientDto dto)
    {
        var client = _mapper.Map<Client>(dto);
        _db.Clients.Add(client);
        await _db.SaveChangesAsync();

        return CreatedAtAction(nameof(GetById), new { id = client.Id }, _mapper.Map<ClientDto>(client));
    }
}
