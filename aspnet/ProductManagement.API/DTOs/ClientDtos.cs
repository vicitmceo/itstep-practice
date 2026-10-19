using System.ComponentModel.DataAnnotations;

namespace ProductManagement.API.DTOs;

/// <summary>Клієнт у відповіді API: без поля Phone.</summary>
public class ClientDto
{
    public int Id { get; set; }
    public string FirstName { get; set; } = string.Empty;
    public string LastName { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
}

/// <summary>Дані для створення клієнта.</summary>
public class CreateClientDto
{
    [Required, StringLength(100)] public string FirstName { get; set; } = string.Empty;
    [Required, StringLength(100)] public string LastName { get; set; } = string.Empty;
    [Required, EmailAddress, StringLength(200)] public string Email { get; set; } = string.Empty;
    [StringLength(30)] public string Phone { get; set; } = string.Empty;
}
