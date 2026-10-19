using System.ComponentModel.DataAnnotations;

namespace ProductManagement.API.DTOs;

public class ProductDto
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string? Description { get; set; }
    public decimal Price { get; set; }
    public int Stock { get; set; }
}

public class CreateProductDto
{
    [Required, StringLength(200)] public string Name { get; set; } = string.Empty;
    [StringLength(1000)] public string? Description { get; set; }
    [Range(0, 1_000_000)] public decimal Price { get; set; }
    [Range(0, 100_000)] public int Stock { get; set; }
}
