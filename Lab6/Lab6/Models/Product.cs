using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Product
    {
        public Product()
        {
            Orders = new HashSet<Order>();
            Features = new HashSet<Feature>();
        }

        public int Id { get; set; }
        public int ModelId { get; set; }
        public int StatusId { get; set; }
        public int WheelId { get; set; }
        public int LightId { get; set; }
        public int EngineId { get; set; }
        public int FeatureId { get; set; }
        public string ExteriorColor { get; set; } = null!;
        public string InteriorColor { get; set; } = null!;
        public string InteriorMaterial { get; set; } = null!;

        public virtual Engine Engine { get; set; } = null!;
        public virtual Light Light { get; set; } = null!;
        public virtual Model Model { get; set; } = null!;
        public virtual ProductStatus Status { get; set; } = null!;
        public virtual Wheel Wheel { get; set; } = null!;
        public virtual ICollection<Order> Orders { get; set; }

        public virtual ICollection<Feature> Features { get; set; }
    }
}
