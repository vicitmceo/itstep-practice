using AutoMapper;
using ProductManagement.API.DTOs;
using ProductManagement.API.Models;

namespace ProductManagement.API.Profiles;

public class MappingProfile : Profile
{
    public MappingProfile()
    {
        CreateMap<Client, ClientDto>();          // Phone в DTO відсутній
        CreateMap<CreateClientDto, Client>();
        CreateMap<Product, ProductDto>();
        CreateMap<CreateProductDto, Product>();
    }
}
