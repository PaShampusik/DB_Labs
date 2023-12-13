using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class OrderStatus
    {
        public OrderStatus()
        {
            Orders = new HashSet<Order>();
        }

        public int Id { get; set; }
        /// <summary>
        /// 1 - done || 0 - processing
        /// </summary>
        public int Status { get; set; }

        public virtual ICollection<Order> Orders { get; set; }
    }
}
