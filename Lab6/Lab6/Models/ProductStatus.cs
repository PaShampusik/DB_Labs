using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class ProductStatus
    {
        public ProductStatus()
        {
            Products = new HashSet<Product>();
        }

        public int Id { get; set; }
        /// <summary>
        /// 1 - in_stock || 0 - not available
        /// </summary>
        public int Status { get; set; }

        public virtual ICollection<Product> Products { get; set; }
    }
}
